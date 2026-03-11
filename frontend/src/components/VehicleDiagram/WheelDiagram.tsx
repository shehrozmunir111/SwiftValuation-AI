import { useFormContext } from 'react-hook-form'
import { useState } from 'react'

const WHEEL_ZONES = [
    { id: 'front_left', label: 'Front Left' },
    { id: 'front_right', label: 'Front Right' },
    { id: 'rear_left', label: 'Rear Left' },
    { id: 'rear_right', label: 'Rear Right' },
    { id: 'spare', label: 'Spare Tire' },
]

const DAMAGE_TYPES = ['Flat', 'Bald', 'Cracked Rim', 'Missing', 'Mismatched']

const WheelDiagram = () => {
    const { setValue, watch } = useFormContext()
    const [selectedZone, setSelectedZone] = useState<string | null>(null)

    const currentDamage = watch('wheel_damage') || []

    const addDamage = (damageType: string, severity: number) => {
        const newDamage = {
            zone_id: selectedZone,
            damage_type: damageType,
            severity,
        }
        setValue('wheel_damage', [...currentDamage, newDamage])
        setSelectedZone(null)
    }

    return (
        <div className="space-y-4">
            <h3 className="font-bold">Wheel & Tire Condition</h3>

            <div className="grid grid-cols-2 gap-2">
                {WHEEL_ZONES.map((zone) => {
                    const hasDamage = currentDamage.some((d: any) => d.zone_id === zone.id)
                    return (
                        <button
                            key={zone.id}
                            type="button"
                            onClick={() => setSelectedZone(zone.id)}
                            className={`p-3 rounded border text-left ${hasDamage ? 'bg-red-100 border-red-300' : 'bg-gray-50'
                                } ${selectedZone === zone.id ? 'ring-2 ring-blue-500' : ''}`}
                        >
                            {zone.label}
                            {hasDamage && <span className="text-red-600 ml-2">●</span>}
                        </button>
                    )
                })}
            </div>

            {selectedZone && (
                <div className="bg-blue-50 p-3 rounded">
                    <p className="text-sm mb-2">Select condition for {selectedZone}:</p>
                    <div className="flex flex-wrap gap-2">
                        {DAMAGE_TYPES.map((type) => (
                            <button
                                key={type}
                                type="button"
                                onClick={() => addDamage(type, 3)}
                                className="px-3 py-1 bg-white border rounded text-sm hover:bg-blue-100"
                            >
                                {type}
                            </button>
                        ))}
                    </div>
                </div>
            )}
        </div>
    )
}

export default WheelDiagram