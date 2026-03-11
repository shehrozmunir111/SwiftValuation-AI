import { useState } from 'react'
import { calculateQuote } from '../utils/api'
import type { QuoteRequest, QuoteResponse } from '../types'

export const useQuote = () => {
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const [quote, setQuote] = useState<QuoteResponse | null>(null)

    const getQuote = async (data: QuoteRequest) => {
        setLoading(true)
        setError(null)

        try {
            const response = await calculateQuote(data)
            setQuote(response)
            return response
        } catch (err: any) {
            setError(err.response?.data?.detail || 'Failed to get quote')
            return null
        } finally {
            setLoading(false)
        }
    }

    const resetQuote = () => {
        setQuote(null)
        setError(null)
    }

    return {
        quote,
        loading,
        error,
        getQuote,
        resetQuote,
    }
}