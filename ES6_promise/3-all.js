function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const response = { message: "Data retrieved"};
            resolve(responseData);
        }, 2000);
        });
    }