class Band:
    """Class representing a musical band."""

    def __init__(self, name, musicians=None):
        """Initialize a Band instance."""
        self.name = name
        self.musicians = musicians if musicians is not None else []

    def __str__(self):
        """Return a string representation of the Band."""
        musicians_str = ', '.join([str(musician) for musician in self.musicians])
        return f"{self.name} ({musicians_str})"

    def play(self):
        """Simulate the band playing."""
        for musician in self.musicians:
            musician.play()


class Musician:
    """Class representing a musician in a band."""

    def __init__(self, name, instruments=None):
        """Initialize a Musician instance."""
        self.name = name
        self.instruments = instruments if instruments is not None else []

    def play(self):
        """Simulate the musician playing an instrument."""
        for instrument in self.instruments:
            print(f"{self.name} is playing: {instrument}")


if __name__ == "__main__":
    # Example usage
    band_name = "Extreme"
    musicians_data = [
        ("Nuno Bettencourt", ["Washburn N4 (1990) : $2,499.95", "Takamine acoustic (1986) : $1,200.00"]),
        ("Gary Cherone", []),
        ("Pat Badger", ["Mouradian CS-74 Bass (2009) : $1,500.00"]),
        ("Kevin Figueiredo", []),
    ]

    musicians = [Musician(name, instruments) for name, instruments in musicians_data]
    my_band = Band(band_name, musicians)

    print(my_band)
    my_band.play()