export default function createInt8TypedArray(length, position, value) {
    if (position < 0 || position >= length) {
        throw new Error('Position outside range');
    }

    const len = new ArrayBuffer(length);
    const data = newData(buffer);
    data.setInt8(position, value);
    return data;
}
