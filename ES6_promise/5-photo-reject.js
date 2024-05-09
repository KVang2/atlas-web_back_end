export default function uploadPhoto(fileName) {
  const errorRejection = `${fileName} cannot be processed`;
  return Promise.reject(new Error(errorRejection));
}
