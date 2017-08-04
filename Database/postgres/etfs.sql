CREATE TABLE "public"."etfs" (
    "ticker" character varying,
    "name" name,
    "expense_ratio" numeric,
    "inception_date" text,
    "strategic_asset_class" text,
    "tactical_asset_class" text,
    "holdings" text,
    "aum_thousands" numeric,
    PRIMARY KEY ("ticker")
);
