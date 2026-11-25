import pytest
import game.redstone_circuit as mod

CASES = [
    ("redstone_path_delay", (1,)),
    ("chunk_state_persist", (1,)),
    ("update_queue_stable_sort", (1,)),
    ("container_read_snapshot", (1,)),
    ("client_predict_rollback", (1,)),
    ("cross_chunk_seq_unify", (1,)),
    ("load_circuit", (1,)),
    ("place_component", (1,)),
    ("step_circuit", (1,)),
    ("present_redstone", (1,)),
    ("validate_redstone", (1,)),
    ("metrics_redstone", (1,)),
    ("audit_redstone", (1,)),
    ("fallback_redstone", (1,)),
    ("determinism_redstone", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
