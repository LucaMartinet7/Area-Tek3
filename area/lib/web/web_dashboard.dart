import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:http/http.dart' as http;
import '../shared/service_box.dart';
import 'web_nav_bar.dart';
import '../shared/user_service.dart';

class Service {
  final String name;
  final String logoPath;
  bool isConnected;
  final String loginUrl;

  Service(this.name, this.logoPath, this.isConnected, this.loginUrl);
}

class WebDashboard extends StatefulWidget {
  const WebDashboard({super.key});

  @override
  WebDashboardState createState() => WebDashboardState();
}

class WebDashboardState extends State<WebDashboard> {
  final List<Service> services = [
    Service('Spotify', 'assets/images/spotify.png', false, 'http://127.0.0.1:8000/api/auth/spotify/login/'),
    Service('Twitch', 'assets/images/twitch.png', false, 'http://127.0.0.1:8000/api/auth/twitch/login/'),
    Service('Google', 'assets/images/google.png', false, 'http://127.0.0.1:8000/api/auth/google/login/'),
  ];

  void handleConnect(String serviceName, String loginUrl) async {
    if (kDebugMode) {
      print('Connecting to $serviceName');
    }
    final Uri loginUri = Uri.parse(loginUrl);
    if (await canLaunchUrl(loginUri)) {
      await launchUrl(loginUri);
      // Await server response for 200 status code
      final response = await http.get(loginUri);
      if (response.statusCode == 302 || response.statusCode == 200) {
        if (kDebugMode) {
          print('Successfully connected to $serviceName');
        }
        setState(() {
          services.firstWhere((service) => service.name == serviceName).isConnected = true;
        });
      } else {
        throw 'Failed to connect to $serviceName: ${response.statusCode}';
      }
    } else {
      throw 'Could not launch $loginUrl';
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const WebNavBar(),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: FutureBuilder<String?>(
            future: getUsername(),
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                return const CircularProgressIndicator();
              } else if (snapshot.hasError || !snapshot.hasData) {
                return const Text('Failed to load username');
              } else {
                final username = snapshot.data!;
                return Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    _buildProfile(context, username),
                    const SizedBox(width: 16),
                    _buildServiceBoxes(services, handleConnect),
                  ],
                );
              }
            },
          ),
        ),
      ),
    );
  }

  Widget _buildProfile(BuildContext context, String username) {
    return Expanded(
      flex: 1,
      child: Container(
        padding: const EdgeInsets.all(16.0),
        decoration: _boxDecoration(),
        child: FutureBuilder<UserProfile>(
          future: fetchUserProfile(username),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return const CircularProgressIndicator();
            } else if (snapshot.hasError) {
              return _buildProfileContent(
                CircleAvatar(
                  radius: 100,
                  child: const Icon(Icons.person, size: 70),
                ),
                'Error',
                'error@example.com',
              );
            } else if (!snapshot.hasData) {
              return _buildProfileContent(
                CircleAvatar(
                  radius: 100,
                  child: const Icon(Icons.person, size: 70),
                ),
                'No Data',
                'nodata@example.com',
              );
            } else {
              final userProfile = snapshot.data!;
              return _buildProfileContent(
                CircleAvatar(
                  radius: 100,
                  backgroundImage: NetworkImage(userProfile.profileImagePath),
                ),
                userProfile.username,
                userProfile.email,
              );
            }
          },
        ),
      ),
    );
  }

  Widget _buildProfileContent(Widget avatar, String username, String email) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const SizedBox(height: 30),
        avatar,
        const SizedBox(height: 30),
        Text(
          "Welcome $username !",
          style: const TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.bold,
            fontFamily: 'ClashGrotesk',
          ),
        ),
        const SizedBox(height: 30),
        Text(
          email,
          style: const TextStyle(
            fontSize: 18,
            color: Colors.grey,
            fontFamily: 'ClashGrotesk',
          ),
        ),
      ],
    );
  }

  Widget _buildServiceBoxes(List<Service> services, void Function(String, String) handleConnect) {
    return Expanded(
      flex: 1,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: services
            .map((service) => ServiceBox(
                  logoPath: service.logoPath,
                  isConnected: service.isConnected,
                  onConnect: () => handleConnect(service.name, service.loginUrl),
                  serviceName: service.name,
                ))
            .toList(),
      ),
    );
  }

  BoxDecoration _boxDecoration() {
    return BoxDecoration(
      color: Colors.white,
      borderRadius: BorderRadius.circular(10),
    );
  }
}