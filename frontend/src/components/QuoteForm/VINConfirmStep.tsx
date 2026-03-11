import { useFormContext } from 'react-hook-form'

const VINConfirmStep = () => {
    const { watch } = useFormContext()
    const vin = watch('vin')
    const year = watch('year')
    const make = watch('make')
    const model = watch('model')

    return (
        <div className="space-y-6">
            <h2 className="text-2xl font-bold text-gray-800">Confirm Vehicle Details</h2>

            <div className="bg-gray-50 p-6 rounded-lg">
                <p className="text-gray-600 mb-2">VIN: <span className="font-mono font-bold">{vin}</span></p>
                <p className="text-2xl font-bold text-gray-800">
                    {year} {make} {model}
                </p>
            </div>

            <p className="text-gray-600">
                Please confirm these details are correct before continuing.
            </p>
        </div>
    )
}

export default VINConfirmStep