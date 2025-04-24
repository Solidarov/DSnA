from factories import AlgorithmFactoryProducer
from services import UserInterface


if __name__ == "__main__":
    ui = UserInterface()

    ui.clear_screen()
    data = ui.get_array_method()

    ui.clear_screen()
    choice_factory = ui.get_user_choice_dict("What to do with the array", 
                                             AlgorithmFactoryProducer.factories)
    factory = AlgorithmFactoryProducer.get_factory(choice_factory)
    
    choice_stragegy = ui.get_user_choice_dict(f"Which method use to {choice_factory}", 
                                              factory.strategies)
    strategy = factory.get_strategy(choice_stragegy)

    ui.clear_screen
    ui.get_results(choice_factory, data, strategy)


