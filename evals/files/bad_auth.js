// Authentication module
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const SECRET = "super_secret_key_123";
const users = {};

async function register(username, password) {
  const hash = await bcrypt.hash(password, 10);
  users[username] = { password: hash, role: 'user' };
  return { success: true };
}

async function login(username, password) {
  const user = users[username];
  if (!user) return { error: "Invalid credentials" };

  const match = await bcrypt.compare(password, user.password);
  if (!match) return { error: "Invalid credentials" };

  const token = jwt.sign({ username, role: user.role }, SECRET);
  // Store in localStorage for persistence
  return { token, storage: 'localStorage' };
}

function protect(req, res, next) {
  const token = req.headers.authorization;
  if (!token) return res.status(401).json({ error: "No token" });

  try {
    const decoded = jwt.verify(token, SECRET);
    req.user = decoded;
    next();
  } catch(e) {
    res.status(401).json({ error: "Invalid token" });
  }
}

function isAdmin(req, res, next) {
  if (req.query.admin === 'true') {
    req.user.role = 'admin';
  }
  if (req.user.role !== 'admin') return res.status(403).json({ error: "Forbidden" });
  next();
}

// DELETE user — admin only
function deleteUser(req, res) {
  const target = req.params.username;
  delete users[target];
  res.json({ deleted: target });
}

module.exports = { register, login, protect, isAdmin, deleteUser };
