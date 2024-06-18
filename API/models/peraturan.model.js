const mongoose = require('mongoose')

const PeraturanSchema = mongoose.Schema({
    judul: {
        type: String
    },
    jenis_bentuk_peraturan: {
        type: String
    },
    pemrakarsa: {
        type: String
    },
    nomor: {
        type: String
    },
    tahun: {
        type: Number
    },
    tentang: {
        type: String
    },
    tempat_penetapan: {
        type: String
    },
    tanggal_penetapan: {
        type: String
    },
    pejabat_penetapan: {
        type: String
    },
    status: {
        type: String
    },
    dokumen_link: {
        type: String
    },
    tahun_pengundangan: {
        type: Number
    },
    no_pengundangan: {
        type: Number
    },
    no_tambahan: {
        type: Number
    },
    tanggal_pengundangan: {
        type: String
    },
    pejabat_pengundangan: {
        type: String
    },
    mengubah: [{
        text: {
            type: String
        },
        link: {
            type: String
        }
    }],
    dasar_hukum: [{
        text: {
            type: String
        },
        link: {
            type: String
        }
    }]
})

const Peraturan = mongoose.model('Peraturan', PeraturanSchema);

module.exports = Peraturan;