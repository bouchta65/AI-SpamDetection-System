import streamlit as st
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

spark = SparkSession.builder.appName("SpamDetectionApp").getOrCreate()

pipeline_path = "models/logistic_pipeline"
pipeline_model = PipelineModel.load(pipeline_path)

st.title("Détecteur de Spam")

text_input = st.text_area("Entrez le texte à tester :")

if st.button("Tester"):
    if text_input.strip() == "":
        st.warning("Veuillez entrer un texte.")
    else:
        df = spark.createDataFrame([(text_input,)], ["text_clean"])
        prediction = pipeline_model.transform(df)
        pred_value = prediction.collect()[0]["prediction"]

        if pred_value == 1:
            st.error("⚠️ Ce message est probablement un SPAM")
        else:
            st.success("✅ Ce message semble HAM (non spam)")
