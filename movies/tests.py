from django.test import TestCase
from django.urls import reverse

from .models import Genre, Movie


class MovieViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.genre = Genre.objects.create(name="Drama")
        cls.movie = Movie.objects.create(
            title="Portfolio Movie",
            release_year=2026,
            number_in_stock=5,
            daily_rate=2.5,
            genre=cls.genre,
        )

    def test_home_page_loads(self):
        response = self.client.get("/", secure=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home")

    def test_movie_list_displays_movie(self):
        response = self.client.get(reverse("movies:index"), secure=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)
        self.assertContains(response, self.genre.name)

    def test_movie_details_display_movie(self):
        response = self.client.get(
            reverse("movies:details", args=[self.movie.pk]),
            secure=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.movie.title)
        self.assertContains(response, self.genre.name)

    def test_missing_movie_returns_404(self):
        response = self.client.get(
            reverse("movies:details", args=[999999]),
            secure=True,
        )

        self.assertEqual(response.status_code, 404)
