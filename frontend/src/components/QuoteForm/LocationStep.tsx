import { useFormContext } from 'react-hook-form'
import Input from '../common/Input'

const LocationStep = () => {
    const { register, formState: { errors } } = useFormContext()

    return (
        <div className="space-y-6">
            <h2 className="text-2xl font-bold text-gray-800">Pickup Location</h2>

            <Input
                label="ZIP Code"
                placeholder="12345"
                {...register('zip_code')}
                error={errors.zip_code?.message as string}
            />

            <Input
                label="City (Optional)"
                placeholder="New York"
                {...register('city')}
            />

            <Input
                label="State (Optional)"
                placeholder="NY"
                {...register('state')}
            />

            <Input
                label="Pickup Address (Optional)"
                placeholder="Full street address"
                {...register('pickup_address')}
            />
        </div>
    )
}

export default LocationStep