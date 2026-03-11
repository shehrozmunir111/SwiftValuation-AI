export interface VehicleInfo {
    vin?: string
    year: number
    make: string
    model: string
    trim?: string
    mileage: number
    title_status: 'clean' | 'salvage' | 'rebuilt' | 'junk' | 'lien'
}

export interface ConditionInfo {
    condition_rating: 'excellent' | 'good' | 'fair' | 'poor' | 'junk'
    drivable: boolean
    engine_issues?: string
    transmission_issues?: string
}

export interface DamageSelection {
    zone_id: string
    damage_type: string
    severity: number
}

export interface LocationInfo {
    zip_code: string
    city?: string
    state?: string
    pickup_address?: string
}

export interface QuoteRequest extends VehicleInfo, ConditionInfo, LocationInfo {
    exterior_damage?: DamageSelection[]
    interior_damage?: DamageSelection[]
    glass_damage?: DamageSelection[]
    wheel_damage?: DamageSelection[]
    classification_hint?: 'junk' | 'auction'
}

export interface QuoteResponse {
    quote_id: string
    classification: 'junk' | 'auction'
    confidence: number
    offer_amount: number | null
    offer_valid_until: string
    partner_id: number | null
    calculation_method: string
    query_time_ms: number
    needs_human_review: boolean
}