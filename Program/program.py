from View.InterfaceRenderer import InterfaceRenderer


class Program:
    """
        The entry class for the application.
    """
    def main(self):
        """
            The method that is the entry point of the whole application.
        """
        InterfaceRenderer().render_interface()


if __name__ == "__main__":
    Program().main()