import { useFormContext } from 'react-hook-form'
import Select from '../common/Select'
import Input from '../common/Input'

const ConditionStep = () => {
    const { register, watch, formState: { errors } } = useFormContext()
    const drivable = watch('drivable')

    return (
        <div className="space-y-6">
            <h2 className="text-2xl font-bold text-gray-800">Vehicle Condition</h2>

            <Select
                label="Overall Condition"
                {...register('condition_rating')}
                error={errors.condition_rating?.message as string}
                options={[
                    { value: 'excellent', label: 'Excellent - Like new' },
                    { value: 'good', label: 'Good - Minor wear' },
                    { value: 'fair', label: 'Fair - Some issues' },
                    { value: 'poor', label: 'Poor - Major issues' },
                    { value: 'junk', label: 'Junk - Not running' },
                ]}
            />

            <div className="space-y-2">
                <label className="block text-sm font-medium text-gray-700">
                    Is the vehicle drivable?
                </label>
                <div className="flex gap-4">
                    <label className="flex items-center gap-2">
                        <input
                            type="radio"
                            value="true"
                            {...register('drivable')}
                            defaultChecked
                        />
                        Yes
                    </label>
                    <label className="flex items-center gap-2">
                        <input
                            type="radio"
                            value="false"
                            {...register('drivable')}
                        />
                        No
                    </label>
                </div>
            </div>

            {!drivable && (
                <>
                    <Input
                        label="Engine Issues (if any)"
                        placeholder="Describe engine problems..."
                        {...register('engine_issues')}
                    />
                    <Input
                        label="Transmission Issues (if any)"
                        placeholder="Describe transmission problems..."
                        {...register('transmission_issues')}
                    />
                </>
            )}
        </div>
    )
}

export default ConditionStep