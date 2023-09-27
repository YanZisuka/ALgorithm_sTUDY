const NULLISH = [undefined, null];

function checkIfInstanceOf(obj: any, classFunction: any): boolean {
  if (NULLISH.some(v => v === obj || v === classFunction)) return false;
  let proto = obj;
  while (Object.getPrototypeOf(proto) !== null) {
    if (Object.getPrototypeOf(proto) === classFunction.prototype) {
      return true;
    }
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
