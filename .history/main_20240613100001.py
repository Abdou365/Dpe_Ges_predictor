from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model_3 import allValueByColumns, predict_dpe_ges

app = FastAPI()
origins = ["*"]

app.add_middleware(
        CORSMiddleware, 
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )

class ReqBody(BaseModel):
    Annee_construction: Optional[int] = None
    Cout_total_5_usages: Optional[float] = None
    Surface_habitable_logement: Optional[float] = None
    Qualite_isolation_enveloppe: Optional[str] = None
    Type_energie_principale_chauffage: Optional[str] = None
    Type_installation_chauffage: Optional[str] = None
    Code_postal_BAN: Optional[int] = None
    Conso_5_usages_e_finale: Optional[float] = None
    Conso_5_usagesm2_e_finale: Optional[float] = None
    Emission_GES_5_usages: Optional[float] = None
    Emission_GES_5_usages_par_m2: Optional[float] = None
    Cout_chauffage: Optional[float] = None
    Cout_ECS: Optional[float] = None
    Qualite_isolation_menuiseries: Optional[str] = None


class PredictionResponse(BaseModel):
    Etiquette_DPE: int
    Etiquette_GES: int

class allValue(BaseModel): 
    Qualite_isolation_enveloppe:list
    Type_energie_principale_chauffage: list
    Type_installation_chauffage:list
    Qualite_isolation_menuiseries: list




@app.get("/dpe/options", response_model=allValue)
async def read_root():
    Qualite_isolation_enveloppe=allValueByColumns['Qualité_isolation_enveloppe']
    Type_energie_principale_chauffage = allValueByColumns['Type_énergie_principale_chauffage']
    Type_installation_chauffage = allValueByColumns['Type_installation_chauffage']
    Qualite_isolation_menuiseries= allValueByColumns['Qualité_isolation_menuiseries']
    return {"Qualite_isolation_enveloppe" : Qualite_isolation_enveloppe, "Type_energie_principale_chauffage": Type_energie_principale_chauffage , "Type_installation_chauffage" : Type_installation_chauffage, "Qualite_isolation_menuiseries" : Qualite_isolation_menuiseries }


@app.post("/", response_model=PredictionResponse)
async def predict(request: ReqBody):
    result = predict_dpe_ges(
        Annee_construction=request.Annee_construction,
        Cout_total_5_usages=request.Cout_total_5_usages,
        Surface_habitable_logement=request.Surface_habitable_logement,
        Qualite_isolation_enveloppe=request.Qualite_isolation_enveloppe,
        Type_energie_principale_chauffage=request.Type_energie_principale_chauffage,
        Type_installation_chauffage=request.Type_installation_chauffage,
        Code_postal_BAN=request.Code_postal_BAN,
        Conso_5_usages_e_finale=request.Conso_5_usages_e_finale,
        Conso_5_usagesm2_e_finale=request.Conso_5_usagesm2_e_finale,
        Emission_GES_5_usages=request.Emission_GES_5_usages,
        Emission_GES_5_usages_par_m2=request.Emission_GES_5_usages_par_m2,
        Cout_chauffage=request.Cout_chauffage,
        Cout_ECS=request.Cout_ECS,
        Qualite_isolation_menuiseries=request.Qualite_isolation_menuiseries
    )
    return result
