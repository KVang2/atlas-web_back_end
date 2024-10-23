const express = require('express');
const app = express();


app.get('/', (req, res) => {
    res.setHeader('Content-Type', 'text/html');
    res.status(200).send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
    const id = req.params.id
    res.status(200).send(`Payment methods for cart ${id}`);
});

app.get('/available_payments', (req, res) => {
    const payment = {
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    };
    res.json(payment);
});

app.post('/login', (req, res) => {
    const { userName } = req.body;
    return res.status(200).json(`Welcome ${userName}`);
});

app.listen(7865, () => {
    console.log('API available on localhost port 7865');
});

module.exports = app;