from dagster import define_asset_job, AssetSelection, AssetKey

indebted_ae_exam_job  = define_asset_job(
    name="indebted_ae_exam_job",
    selection=AssetSelection.all()
)