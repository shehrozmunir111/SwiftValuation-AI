import axios from 'axios'

const api = axios.create({
    baseURL: '/api/v1',
    headers: {
        'Content-Type': 'application/json',
    },
})

export const calculateQuote = async (data: any) => {
    const response = await api.post('/quotes/calculate', data)
    return response.data
}

export const getVehicleMakes = async (year?: number) => {
    const response = await api.get('/vehicles/makes', { params: { year } })
    return response.data.makes
}

export const getVehicleModels = async (make: string, year?: number) => {
    const response = await api.get('/vehicles/models', { params: { make, year } })
    return response.data.models
}

export const lookupVIN = async (vin: string) => {
    const response = await api.get('/vehicles/lookup', { params: { vin } })
    return response.data
}

export default api