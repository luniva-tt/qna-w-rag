
from sentence_transformers import util

def evaluate_answer(pred, true, model):
    pred_emb = model.encode(pred, convert_to_tensor=True)
    true_emb = model.encode(true, convert_to_tensor=True)
    return util.cos_sim(pred_emb, true_emb).item()
