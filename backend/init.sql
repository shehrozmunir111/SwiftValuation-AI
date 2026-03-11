-- Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Performance indexes
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_quotes_status_created 
ON quotes(status, created_at DESC);

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_partners_coverage 
ON partners USING GIN(coverage_zips);

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_pricing_rules_lookup 
ON pricing_rules(partner_id, vehicle_id, is_active) 
WHERE rule_type = 'vehicle_specific';