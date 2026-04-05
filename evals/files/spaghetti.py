import os, sys, json, time, random, hashlib, base64, re
from datetime import datetime

data = {}
cache = {}
log = []
errs = []

def proc(x, mode=None, fmt='json', verbose=False, retry=3, timeout=30, callback=None, flags=None):
    global data, cache, log, errs
    if flags is None:
        flags = {}
    result = None
    t = time.time()
    if verbose:
        print(f"[{datetime.now()}] Processing {x} with mode={mode}")
    try:
        if mode == 'load':
            if x in cache:
                result = cache[x]
                if verbose:
                    print(f"  Cache hit for {x}")
            else:
                if os.path.exists(x):
                    with open(x) as f:
                        if fmt == 'json':
                            result = json.load(f)
                        elif fmt == 'text':
                            result = f.read()
                        elif fmt == 'lines':
                            result = f.readlines()
                        elif fmt == 'csv':
                            result = [l.strip().split(',') for l in f.readlines()]
                        else:
                            result = f.read()
                    cache[x] = result
                    data[x] = result
                else:
                    errs.append(f"File not found: {x}")
                    if retry > 0:
                        time.sleep(1)
                        return proc(x, mode, fmt, verbose, retry-1, timeout, callback, flags)
                    result = None
        elif mode == 'save':
            if fmt == 'json':
                with open(x, 'w') as f:
                    json.dump(data.get(flags.get('key', x), {}), f, indent=2)
            elif fmt == 'text':
                with open(x, 'w') as f:
                    f.write(str(data.get(flags.get('key', x), '')))
            else:
                with open(x, 'w') as f:
                    f.write(str(data.get(flags.get('key', x), '')))
            result = True
        elif mode == 'transform':
            d = data.get(x, cache.get(x))
            if d is None:
                errs.append(f"No data for key {x}")
                return None
            op = flags.get('op', 'identity')
            if op == 'uppercase':
                result = str(d).upper()
            elif op == 'lowercase':
                result = str(d).lower()
            elif op == 'reverse':
                result = str(d)[::-1]
            elif op == 'hash':
                result = hashlib.sha256(str(d).encode()).hexdigest()
            elif op == 'base64':
                result = base64.b64encode(str(d).encode()).decode()
            elif op == 'count':
                result = len(d) if hasattr(d, '__len__') else 1
            elif op == 'sort':
                result = sorted(d) if isinstance(d, list) else d
            elif op == 'unique':
                result = list(set(d)) if isinstance(d, list) else d
            elif op == 'flatten':
                if isinstance(d, list):
                    result = []
                    for item in d:
                        if isinstance(item, list):
                            for subitem in item:
                                result.append(subitem)
                        else:
                            result.append(item)
                else:
                    result = d
            elif op == 'filter':
                pattern = flags.get('pattern', '.*')
                if isinstance(d, list):
                    result = [i for i in d if re.match(pattern, str(i))]
                elif isinstance(d, dict):
                    result = {k:v for k,v in d.items() if re.match(pattern, str(k))}
                else:
                    result = d
            elif op == 'identity':
                result = d
            else:
                errs.append(f"Unknown op: {op}")
                result = d
            data[x] = result
        elif mode == 'analyze':
            d = data.get(x, cache.get(x))
            if d is None:
                return None
            result = {
                'type': type(d).__name__,
                'size': len(d) if hasattr(d, '__len__') else 1,
                'sample': str(d)[:100],
                'hash': hashlib.md5(str(d).encode()).hexdigest(),
            }
        elif mode == 'batch':
            items = flags.get('items', [])
            results = []
            for item in items:
                r = proc(item.get('x', x), item.get('mode', 'load'), item.get('fmt', fmt),
                         verbose, retry, timeout, callback, item.get('flags', {}))
                results.append(r)
            result = results
        elif mode == 'pipeline':
            steps = flags.get('steps', [])
            current = x
            for step in steps:
                current = proc(current, step.get('mode'), step.get('fmt', fmt),
                              verbose, retry, timeout, callback, step.get('flags', {}))
                if current is None:
                    errs.append(f"Pipeline broke at step {step}")
                    break
            result = current
        else:
            if x and os.path.exists(str(x)):
                result = proc(x, 'load', fmt, verbose, retry, timeout, callback, flags)
            else:
                data[str(x)] = x
                result = x

        elapsed = time.time() - t
        log.append({'action': mode, 'target': str(x)[:50], 'elapsed': elapsed, 'ok': result is not None})
        if callback:
            callback(result)
        if verbose:
            print(f"  Done in {elapsed:.3f}s")
        return result
    except Exception as e:
        errs.append(f"{mode} failed on {x}: {e}")
        log.append({'action': mode, 'target': str(x)[:50], 'elapsed': time.time()-t, 'ok': False, 'error': str(e)})
        if retry > 0:
            time.sleep(0.5)
            return proc(x, mode, fmt, verbose, retry-1, timeout, callback, flags)
        return None

def status():
    return {'data_keys': list(data.keys()), 'cache_keys': list(cache.keys()),
            'log_count': len(log), 'error_count': len(errs), 'errors': errs[-5:]}

if __name__ == '__main__':
    proc('config.json', 'load')
    proc('config.json', 'transform', flags={'op': 'hash'})
    print(status())
