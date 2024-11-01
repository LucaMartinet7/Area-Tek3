import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../shared/service_box.dart';
import 'web_nav_bar.dart';

class Service {
  final String name;
  final String logoPath;
  final bool isConnected;
  final String description; // Add description field

  Service(this.name, this.logoPath, this.isConnected, this.description);
}

class UserProfile {
  final String username;
  final String email;
  final String profileImagePath;
  UserProfile({required this.username, required this.email, required this.profileImagePath});
  factory UserProfile.fromJson(Map<String, dynamic> json) {
    return UserProfile(
      username: json['username'],
      email: json['email'],
      profileImagePath: json['profile_image'] ?? 'assets/images/profile/profile.png',
    );
  }
}

class WebDashboard extends StatelessWidget {
  const WebDashboard({super.key});

  Future<UserProfile> fetchUserProfile(String username) async {
    final response = await http.get(Uri.parse('http://127.0.0.1:8000/api/auth/auth/user-info/$username/'));
    if (response.statusCode == 200) {
      return UserProfile.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to load user profile');
    }
  }

  Future<String?> getUsername() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString('username');
  }

  @override
  Widget build(BuildContext context) {
    final services = [
      Service('Spotify', 'assets/images/spotify.png', true, 'Stream music and podcasts.'),
      Service('Twitch', 'assets/images/twitch.png', false, 'Watch live streams and gaming videos.'),
      Service('Google', 'assets/images/google.png', true, 'Search the web and use various Google services.'),
      Service('Microsoft', 'assets/images/microsoft.png', true, 'Access Microsoft services and products.'),
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
                  child: const Icon(Icons.person, size: 150),
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
          style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 30),
        Text(
          email,
          style: const TextStyle(fontSize: 18, color: Colors.grey),
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