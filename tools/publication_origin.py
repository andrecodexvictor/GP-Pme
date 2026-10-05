"""Metadados de origem portáveis; os originais completos permanecem no backup."""
import json
from tools.editorial import ROOT

def origin(path):
    registry=ROOT/'framework/publicacao/origens.json'
    return json.loads(registry.read_text(encoding='utf-8')).get(path,{}) if registry.exists() else {}
