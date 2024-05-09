export default function getResponseFromAPI(promise) {
  return promise
    .then(response => {
        return { status: 200, body: 'Success' };
    })

    .catch(error => {
      return new Error();
  })

  .finally(() => {
    console.log("Got a respose from the API");
  });
}
