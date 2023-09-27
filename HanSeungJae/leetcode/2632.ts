function curry(f: Function): Function {
  function fix(arity: number, f: Function) {
    return Object.defineProperty(f, 'length', { value: arity });
  }

  return (...xs: unknown[]) => {
    if (f.length <= xs.length) return f(...xs);
    return curry(
      fix(f.length - xs.length, (...ys: unknown[]) => f(...xs, ...ys))
    );
  };
}
