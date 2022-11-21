"""
Songnova search engine
"""
from ytmusicapi import YTMusic  # type: ignore


class Search:
    """
    Search engine for Songnova
    """

    def __init__(self):
        """
        Initialize the search engine
        """
        self.api = YTMusic()

    def search_songs(self, query: str) -> list:
        """
        Search for songs
        :param query: Song name/title
        :return: list of dictionary data
        sample return data:
        {'album': {'id': 'MPREb_9tfMjCSs2wF', 'name': 'Lovestrong.'},
        'artists': [{'id': 'UCunB7BiOZ7aN6v6TgCp5dRA', 'name': 'christina perri'}],
        'duration': '3:54',
        'thumbnails': [{'height': 60,
                 'url': 'https://lh3.googleusercontent.com/cBLuwMC5KuIz90Bn9rmYBC
                        jk5fRuMLPKpQwbJynOxLsAzBtj73zZdkOGGZk
                        2hQNMDbX
                        iff_JEEksZjd4=w60-h60-l90-rj',
                 'width': 60},
                {'height': 120,
                 'url': 'https://lh3.googleusercontent.com/cBLuwMC5Ku
                        Iz90Bn9rmYBCjk5fRuMLPKpQwbJynOxLsAzBtj7
                        3zZdkOGGZk2hQNMDbXiff_JEEksZjd4=w120-h120-l90-rj',
                 'width': 120}],
        'title': 'the lonely',
        'videoId': 'XULJqPb_pNU',
        'year': None}
        """
        keys: list = [
            "category",
            "resultType",
            "duration_seconds",
            "isExplicit",
            "feedbackTokens",
            "videoType"
        ]
        results: list = self.api.search(query, filter="songs")
        for result in results:
            for key in keys:
                del result[key]
        return results
