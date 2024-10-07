import 'package:flutter/foundation.dart';

bool isMobile() {
  return !kIsWeb && (defaultTargetPlatform == TargetPlatform.android);
}