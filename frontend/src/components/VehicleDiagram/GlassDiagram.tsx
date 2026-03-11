import { useFormContext } from 'react-hook-form'
import { useState } from 'react'

const GLASS_ZONES = [
    { id: 'windshield', label: 'Windshield' },
    { id: 'rear_window', label: 'Rear Window' },
    { id: 'driver_front', label: 'Driver Front' },
    { id: 'driver_rear', label: 'Driver Rear' },
    { id: 'passenger_front', label: 'Passenger Front' },
    { id: 'passenger_rear', label: 'Passenger Rear' },
]

const DAMAGE_TYPES = ['Crack', 'Chip', 'Shattered', 'Tint Damage']

const GlassDiagram = () => {
    const { setValue, watch } = useFormContext()
    const [selectedZone, setSelectedZone] = useState<string | null>(null)

    const currentDamage = watch('glass_damage') || []

    const addDamage = (damageType: string, severity: number) => {
        const newDamage = {
            zone_id: selectedZone,
            damage_type: damageType,
            severity,
        }
        setValue('glass_damage', [...currentDamage, newDamage])
        setSelectedZone(null)
    }

    return (
        <div className="space-y-4">
            <h3 className="font-bold">Glass Damage</h3>

            <div className="grid grid-cols-2 gap-2">
                {GLASS_ZONES.map((zone) => {
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
                    <p className="text-sm mb-2">Select damage for {selectedZone}:</p>
                    <div className="flex flex-wrap gap-2">
                        {DAMAGE_TYPES.map((type) => (
                            [1, 2, 3].map((sev) => (
                                <button
                                    key={`${type}-${sev}`}
                                    type="button"
                                    onClick={() => addDamage(type, sev)}
                                    className="px-3 py-1 bg-white border rounded text-sm hover:bg-blue-100"
                                >
                                    {type} {sev}
                                </button>
                            ))
                        ))}
                    </div>
                </div>
            )}
        </div>
    )
}

export default GlassDiagram