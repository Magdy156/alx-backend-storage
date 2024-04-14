-- Creates an index idx_name_first on table names and 1st letter of name
-- Only first letter of name must be indexed

CREATE INDEX idx_name_first_score
ON names(name(1), score);
