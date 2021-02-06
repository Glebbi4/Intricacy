# Indiana Jones and the Jun-Xi Ring
In one eastern market, Indiana Jones got an interesting document. It mentioned a mysterious ring that belonged to the famous military strategist of antiquity Jun-Xi and, according to the author, somehow absorbed some of his wisdom. The ring was probably passed from one Chinese emperor to another and was eventually buried with one of them.

To verify this information, you must visit the Imperial Tombs, which are a intricacy of rooms and passages. The Chinese authorities do not allow any research to be conducted there. But through an acquaintance in the Ministry of Culture, Dr. Jones received permission to launch a research robot to search for the artifact.

## Need to do
You need to compose the intricacy_controller () function to control the robot. It is known that the labyrinth is square, somewhere in it should be a ring of Jun-Xi and all. The plan of the labyrinth and its exact dimensions, as well as the exact location of the entrance and the desired artifact, are unknown.

Unfortunately, instead of the latest WOLLY-3000, Dr. Jones was sold a cheaper BALLY-3000, the disadvantages of which are the very limited range of sensors and the lack of a built-in mapping function. Therefore, the existing robot "sees" only what is only directly in front of it and determines the presence of obstacles on the road only in direct contact with them.

The robot has an object-oriented control interface with the following methods:

 * go () - drive forward on the field, returns True or False depending on whether you managed to drive (for example, there may be a wall in front of the robot). If it is impossible to pass, the robot remains in place.
 * turn_left () - rotate 90 degrees counterclockwise.
 * turn_right () - rotate 90 degrees clockwise.
 * found () - checks if the ring is in sight of the robot.
	
As the only argument when calling the intricacy_controller () function, an initialized object of class intricacyRunner is passed to control the robot. The intricacy_controller function does not return anything using the return statement. But as a result of her work, the robot must be transferred to the field of the labyrinth, which contains the desired artifact (assume that the artifact is always present in the intricacy). That is, after calling intricacy_controller (intricacy_runner), the method of the intricacy_runner.found () object must return True. Direct access to the image of the intricacy is prohibited.
