-- Optimize simple search
-- create index on table
CREATE INDEX idx_name_first ON names (name(1));