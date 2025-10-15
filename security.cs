// Author: Steve Sekapin Mnouze
// File: Security.cs
// Description: Implements password validation and UUIDv4 generation.

using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace Assignment2
{
    public static class Security
    {
        /// <summary>
        /// Checks if the given password meets basic security requirements.
        /// Must be at least 8 characters, contain upper, lower, digit, and special char.
        /// </summary>
        public static bool CheckPassword(string password)
        {
            if (string.IsNullOrEmpty(password))
                return false;

            if (password.Length < 8)
                return false;

            if (!password.Any(char.IsUpper))
                return false;

            if (!password.Any(char.IsLower))
                return false;

            if (!password.Any(char.IsDigit))
                return false;

            if (!password.Any(ch => !char.IsLetterOrDigit(ch)))
                return false;

            return true;
        }

        /// <summary>
        /// Generates a valid version-4 UUID string.
        /// </summary>
        public static string GenerateUUIDv4()
        {
            return Guid.NewGuid().ToString();
        }
    }
}

