import 'package:loginui_android_dart/Components/my_textfield.dart';
import 'package:loginui_android_dart/Components/square_tiles.dart';
import 'package:flutter_neumorphic_plus/flutter_neumorphic.dart';

class SignIn extends StatefulWidget {
  const SignIn({super.key});

  @override
  State<SignIn> createState() => SignInState();
}

class SignInState extends State<SignIn> {
  final username = TextEditingController();
  final password = TextEditingController();
  static const String usernameKey = 'Username';
  static const String passwordKey = 'Password';
  void goToHome() {}
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: SingleChildScrollView(
          child: SafeArea(
            child: Column(
              children: [
                const SizedBox(
                  height: 15,
                ),
                ClipRRect(
                  borderRadius: BorderRadius.circular(10),
                  child: Image.asset('Images/user2.webp',width:100,),
                ),
                const SizedBox(height: 30),
                const Text(
                  'Welcome!, Let\'s get started by signing in first.',
                  style: TextStyle(
                      fontFamily: 'Solitreo',
                      fontSize: 18,
                      color: Colors.black),
                ),
                const SizedBox(
                  height: 20,
                ),
                SizedBox(
                  height: MediaQuery.of(context).size.height*0.15,
                  width:MediaQuery.of(context).size.width*0.9,
                  child: Column(
                    children: [
                      const SizedBox(
                        height: 10,
                      ),
                      MyTextField(
                          controllers: username,
                          hintText: 'Username or Email',
                          obscureText: false),
                      const SizedBox(
                        height: 10,
                      ),
                      MyTextField(
                        hintText: 'Password',
                        obscureText: true,
                        controllers: password,
                      ),
                    ],
                  ),
                ),
                Padding(
                  padding: EdgeInsets.only(right: MediaQuery.of(context).size.width*0.1),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      Text(
                        'Forgot Password?',
                        style: TextStyle(
                          color: Colors.grey[700],
                          fontFamily: 'Solitreo',
                        ),
                      ),
                    ],
                  ),
                ),
                NeumorphicButton(
                  onPressed: () {},
                  style: const NeumorphicStyle(depth: 5),
                  child: const Text(
                    'Sign In',
                    style: TextStyle(
                        fontFamily: 'Solitreo',
                        fontSize: 24,
                        color: Colors.black),
                  ),
                ),
                const SizedBox(
                  height: 20,
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 25.0),
                  child: Row(
                    children: [
                      const Expanded(
                        child: Divider(
                          thickness: 2.5,
                          color: Color.fromARGB(255, 7, 1, 1),
                        ),
                      ),
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 10.0),
                        child: Text(
                          'Or continue with',
                          style: TextStyle(
                            color: Colors.grey[800],
                            fontSize: 16,
                            fontFamily: 'Solitreo',
                          ),
                        ),
                      ),
                      const Expanded(
                        child: Divider(
                          thickness: 2.5,
                          color: Color.fromARGB(255, 7, 1, 1),
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(
                  height: 20,
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    NeumorphicButton(
                      onPressed: () => goToHome(),
                      style: const NeumorphicStyle(depth: 5),
                      child:
                          const SquareTile(imagePath: 'Images/Google.jpg'),
                    ),
                    const SizedBox(
                      width: 30,
                    ),
                    NeumorphicButton(
                        onPressed: () => goToHome(),
                        style: const NeumorphicStyle(depth: 5),
                        child: const SquareTile(
                            imagePath: 'Images/Apple.jpg')),
                  ],
                ),
                const SizedBox(
                  height: 20,
                ),
                const Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(
                      'Not a member ?',
                      style: TextStyle(
                          fontFamily: 'Solitreo',
                          fontSize: 15,
                          color: Colors.black),
                    ),
                    SizedBox(
                      width: 10,
                    ),
                    Text(
                      'Register Now ',
                      style: TextStyle(
                        color: Colors.blueAccent,
                        fontFamily: 'Solitreo',
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
