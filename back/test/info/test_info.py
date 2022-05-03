from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.info import InfoRepository, Info


def test_should_return_info_in_database():
    info_repository = InfoRepository(temp_file())
    app = create_app(repositories={"info": info_repository})
    client = app.test_client()

    info_repository.save(
        Info(
            app_name="test application",
        )
    )

    response = client.get("/api/info")
    assert response.json == {
        "app_name": "test application",
    }
