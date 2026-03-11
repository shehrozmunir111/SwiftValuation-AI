import { useFormContext } from 'react-hook-form'
import { useEffect, useState } from 'react'
import Input from '../common/Input'
import Select from '../common/Select'
import { getVehicleMakes, getVehicleModels, lookupVIN } from '../../utils/api'

const VehicleInfoStep = () => {
    const { register, watch, setValue, formState: { errors } } = useFormContext()
    const [makes, setMakes] = useState<string[]>([])
    const [models, setModels] = useState<string[]>([])
    const [vinLoading, setVinLoading] = useState(false)

    const year = watch('year')
    const make = watch('make')
    const vin = watch('vin')

    useEffect(() => {
        getVehicleMakes(year).then(setMakes)
    }, [year])

    useEffect(() => {
        if (make) {
            getVehicleModels(make, year).then(setModels)
        }
    }, [make, year])

    const handleVINLookup = async () => {
        if (!vin || vin.length !== 17) return

        setVinLoading(true)
        try {
            const data = await lookupVIN(vin)
            if (data.year) setValue('year', data.year)
            if (data.make) setValue('make', data.make)
            if (data.model) setValue('model', data.model)
        } finally {
            setVinLoading(false)
        }
    }

    const currentYear = new Date().getFullYear()
    const years = Array.from({ length: currentYear - 1900 + 1 }, (_, i) => currentYear - i)

    return (
        <div className="space-y-6">
            <h2 className="text-2xl font-bold text-gray-800">Vehicle Information</h2>

            <div className="flex gap-2">
                <Input
                    label="VIN (Optional)"
                    placeholder="17-character VIN"
                    {...register('vin')}
                    error={errors.vin?.message as string}
                />
                <Button
                    type="button"
                    variant="secondary"
                    onClick={handleVINLookup}
                    isLoading={vinLoading}
                    className="mt-6"
                >
                    Lookup
                </Button>
            </div>

            <Select
                label="Year"
                {...register('year', { valueAsNumber: true })}
                error={errors.year?.message as string}
                options={years.map(y => ({ value: y.toString(), label: y.toString() }))}
            />

            <Select
                label="Make"
                {...register('make')}
                error={errors.make?.message as string}
                options={makes.map(m => ({ value: m, label: m }))}
            />

            <Select
                label="Model"
                {...register('model')}
                error={errors.model?.message as string}
                options={models.map(m => ({ value: m, label: m }))}
            />

            <Input
                label="Mileage"
                type="number"
                {...register('mileage', { valueAsNumber: true })}
                error={errors.mileage?.message as string}
            />

            <Select
                label="Title Status"
                {...register('title_status')}
                error={errors.title_status?.message as string}
                options={[
                    { value: 'clean', label: 'Clean' },
                    { value: 'salvage', label: 'Salvage' },
                    { value: 'rebuilt', label: 'Rebuilt' },
                    { value: 'junk', label: 'Junk' },
                    { value: 'lien', label: 'Lien' },
                ]}
            />
        </div>
    )
}

// Button import ke liye
import Button from '../common/Button'

export default VehicleInfoStep