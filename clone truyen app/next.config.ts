import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  experimental: {
    // some versions of Next 15+ have it here
  },
  // the log specifically said:
  allowedDevOrigins: ['192.168.1.99', '0.0.0.0', 'localhost', '127.0.0.1'],
} as any;

export default nextConfig;
