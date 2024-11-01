import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import '../shared/service_box.dart';
import '../shared/user_service.dart';
import 'mobile_nav_bar.dart';
import '../shared/exit_button.dart' show buildExitButton;

class Service {
  final String name;
  final String logoPath;
  final bool isConnected;

  Service(this.name, this.logoPath, this.isConnected);
}

class MobileAccount extends StatelessWidget {
  const MobileAccount({super.key});

  @override
  Widget build(BuildContext context) {
    final services = [
      Service('Spotify', 'assets/images/spotify.png', true),
      Service('Twitch', 'assets/images/twitch.png', false),
      Service('Google', 'assets/images/google.png', true),
      Service('Microsoft', 'assets/images/microsoft.png', true),
    ];

    void handleConnect(String serviceName) {
      if (kDebugMode) {
        print('Connecting to $serviceName');
      }
    }

    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        actions: [
          buildExitButton(context),
        ],
      ),
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
                return Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    _buildProfile(context, username),
                    const SizedBox(height: 16),
                    _buildServiceBoxes(services, handleConnect),
                  ],
                );
              }
            },
          ),
        ),
      ),
      bottomNavigationBar: const MobileNavBar(),
    );
  }

  Widget _buildProfile(BuildContext context, String username) {
    return Container(
      width: double.infinity, // Make the container take the full width of the screen
      padding: const EdgeInsets.all(16.0),
      child: FutureBuilder<UserProfile>(
        future: fetchUserProfile(username),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const CircularProgressIndicator();
          } else if (snapshot.hasError) {
            return _buildProfileContent(
              CircleAvatar(
                radius: 50,
                child: const Icon(Icons.person, size: 50),
              ),
              'Error',
              'error@example.com',
            );
          } else if (!snapshot.hasData) {
            return _buildProfileContent(
              CircleAvatar(
                radius: 50,
                child: const Icon(Icons.person, size: 50),
              ),
              'No Data',
              'nodata@example.com',
            );
          } else {
            final userProfile = snapshot.data!;
            return _buildProfileContent(
              CircleAvatar(
                radius: 50,
                backgroundImage: NetworkImage(userProfile.profileImagePath),
              ),
              userProfile.username,
              userProfile.email,
            );
          }
        },
      ),
    );
  }

  Widget _buildProfileContent(Widget avatar, String username, String email) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const SizedBox(height: 10),
        avatar,
        const SizedBox(height: 10),
        Text(
          "Welcome $username !",
          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 10),
        Text(
          email,
          style: const TextStyle(fontSize: 14, color: Colors.grey),
        ),
      ],
    );
  }

  Widget _buildServiceBoxes(List<Service> services, void Function(String) handleConnect) {
    return Expanded(
      child: ListView.builder(
        padding: const EdgeInsets.all(20.0),
        itemCount: services.length,
        itemBuilder: (context, index) {
          final service = services[index];
          return Card(
            margin: const EdgeInsets.symmetric(vertical: 20.0),
            child: Center(
              child: Container(
                constraints: const BoxConstraints(
                  maxHeight: 80,
                ),
                child: ServiceBox(
                  logoPath: service.logoPath,
                  isConnected: service.isConnected,
                  serviceName: service.name,
                  onConnect: () => handleConnect(service.name),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}