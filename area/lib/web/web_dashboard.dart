import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import '../shared/service_box.dart';
import 'web_nav_bar.dart';
import '../shared/user_service.dart';

class Service {
  final String name;
  final String logoPath;
  final bool isConnected;

  Service(this.name, this.logoPath, this.isConnected, );
}

class WebDashboard extends StatelessWidget {
  const WebDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    final services = [
      Service('Spotify', 'assets/images/spotify.png', false),
      Service('Twitch', 'assets/images/twitch.png', true),
      Service('Google', 'assets/images/google.png', false),
      Service('Microsoft', 'assets/images/microsoft.png', true),
    ];

    void handleConnect(String serviceName) {
      if (kDebugMode) {
        print('Connecting to $serviceName');
      }
    }

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

  Widget _buildServiceBoxes(List<Service> services, void Function(String) handleConnect) {
    return Expanded(
      flex: 1,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: services
            .map((service) => ServiceBox(
                  logoPath: service.logoPath,
                  isConnected: service.isConnected,
                  onConnect: () => handleConnect(service.name),
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