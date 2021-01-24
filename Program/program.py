from View.interface_renderer import InterfaceRenderer


class Program:
    """
        The entry class for the application.
    """

    def main(self):
        """
            The method that is the entry point of the whole application.
        """
        # Builds the interface and starts the application
        InterfaceRenderer().render_interface()

# Driver function for the program
if __name__ == "__main__":
    # Calls the above main method when the user runs the program
    Program().main()