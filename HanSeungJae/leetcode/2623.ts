type Fn = (...params: number[]) => number;

function memoize(fn: Fn): Fn {
  const _memo = new Map<string, ReturnType<Fn>>();
  return function (...args) {
    const key = JSON.stringify(args);
    if (_memo.has(key)) {
      return _memo.get(key)!;
    }
    const result = fn(...args);
    _memo.set(key, result);
    return result;
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
