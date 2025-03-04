
def test_ipykernel_installed():
    try:
        import ipykernel
        assert isinstance(ipykernel, object)
    except ModuleNotFoundError:
        assert False, "ipykernel not installed"

def test_vertexai_access():
    from vertexai.generative_models import GenerativeModel
    model = GenerativeModel(model_name="gemini-2.0-flash-lite-001")
    response = model.generate_content("Hello, world!")
    assert len(response.text) > 0