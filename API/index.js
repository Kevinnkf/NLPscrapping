const express = require('express')
const mongoose = require('mongoose')
const app = express()

app.use(express.json())

// Models
const Peraturan = require('./models/peraturan.model.js')

app.get('/', (req, res) => {
    res.send('Hello')
})

// Add Peraturan
app.post('/api/peraturan', async(req, res) => {
    try {
        const peraturan = await Peraturan.create(req.body)
        res.status(200).json(peraturan)
    } catch(error){
        res.status(500).json({message: error.message})
    }
})

// Get All Data
app.get('/api/peraturan',  async (req, res) => {
    try{
        const peraturan = await Peraturan.find({})
        res.status(200).json(peraturan)
    } catch(error) {
        res.status(500).json({message: error.message})
    }
})

// Get Peraturan Base on ID
app.get('/api/peraturan/:id',  async (req, res) => {
    try{
        const {id} = req.params
        const peraturan = await Peraturan.findById(id)
        res.status(200).json(peraturan)
    } catch(error) {
        res.status(500).json({message: error.message})
    }
})

// Connect to MongoDB
mongoose
.connect('mongodb+srv://legalscope:1aqmOffieW80dCeb@legalscopedb.ygg9klj.mongodb.net/Legal-Scope-API?retryWrites=true&w=majority&appName=LegalScopeDB')
.then(() => {
    console.log('Connected to MongoDB')
    app.listen(3000, () => {
        console.log('Server listening on http://127.0.0.1:3000')
    })
}).catch((error) => {
    console.log('Connection failed: ', error)
})
