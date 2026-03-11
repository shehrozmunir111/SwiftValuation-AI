import { useState, useRef, useCallback } from 'react'

export const useCamera = () => {
    const videoRef = useRef<HTMLVideoElement>(null)
    const [stream, setStream] = useState<MediaStream | null>(null)
    const [error, setError] = useState<string | null>(null)

    const startCamera = useCallback(async () => {
        try {
            const mediaStream = await navigator.mediaDevices.getUserMedia({
                video: { facingMode: 'environment' },
                audio: false,
            })

            if (videoRef.current) {
                videoRef.current.srcObject = mediaStream
            }
            setStream(mediaStream)
            setError(null)
        } catch (err) {
            setError('Camera access denied. Please allow camera permissions.')
        }
    }, [])

    const stopCamera = useCallback(() => {
        if (stream) {
            stream.getTracks().forEach(track => track.stop())
            setStream(null)
        }
    }, [stream])

    const capturePhoto = useCallback((): string | null => {
        if (!videoRef.current) return null

        const canvas = document.createElement('canvas')
        canvas.width = videoRef.current.videoWidth
        canvas.height = videoRef.current.videoHeight

        const ctx = canvas.getContext('2d')
        ctx?.drawImage(videoRef.current, 0, 0)

        return canvas.toDataURL('image/jpeg', 0.9)
    }, [])

    return {
        videoRef,
        stream,
        error,
        startCamera,
        stopCamera,
        capturePhoto,
    }
}