var TimeLimitedCache = function () {
  this._cache = new Map();
  this._timer = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  if (this._cache.has(key)) {
    this._cache.set(key, value);
    clearTimeout(this._timer.get(key));
    const id = setTimeout(() => {
      this._cache.delete(key);
      this._timer.delete(key);
    }, duration);
    this._timer.set(key, id);
    return true;
  }
  this._cache.set(key, value);
  const id = setTimeout(() => {
    this._cache.delete(key);
    this._timer.delete(key);
  }, duration);
  this._timer.set(key, id);
  return false;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  return this._cache.get(key) ?? -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  return this._cache.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
