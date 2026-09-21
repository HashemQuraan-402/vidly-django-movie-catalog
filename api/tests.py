from django.test import TestCase
from tastypie.authorization import ReadOnlyAuthorization

from movies.models import Genre, Movie

from .models import MovieResource


class MovieApiTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        genre = Genre.objects.create(name="Science Fiction")
        cls.movie = Movie.objects.create(
            title="API Test Movie",
            release_year=2026,
            number_in_stock=3,
            daily_rate=3.5,
            genre=genre,
        )

    def test_movie_api_returns_catalog_data(self):
        response = self.client.get(
            "/api/movies/",
            secure=True,
            HTTP_ACCEPT="application/json",
        )

        self.assertEqual(response.status_code, 200)

        payload = response.json()
        self.assertEqual(payload["objects"][0]["title"], self.movie.title)
        self.assertNotIn("date_created", payload["objects"][0])

    def test_movie_api_uses_read_only_authorization(self):
        resource = MovieResource()

        self.assertIsInstance(
            resource._meta.authorization,
            ReadOnlyAuthorization,
        )
