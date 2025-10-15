// Author: Steve Sekapin Mnouze
// File: SecurityTests.cs

using Xunit;
using Assignment2;

namespace Assignment2Tests
{
    public class SecurityTests
    {
        [Fact]
        public void TestValidPassword()
        {
            Assert.True(Security.CheckPassword("Valid123!"));
        }

        [Fact]
        public void TestInvalidPasswords()
        {
            Assert.False(Security.CheckPassword("Va1"));           // too short
            Assert.False(Security.CheckPassword("valid123!"));      // no uppercase
            Assert.False(Security.CheckPassword("VALID123!"));      // no lowercase
            Assert.False(Security.CheckPassword("ValidPass!"));     // no digit
            Assert.False(Security.CheckPassword("Valid123"));       // no special char
        }

        [Fact]
        public void TestUUIDv4Format()
        {
            var uuid = Security.GenerateUUIDv4();
            // Regex for UUIDv4 format
            Assert.Matches(@"^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-4[0-9a-fA-F]{3}\-[89abAB][0-9a-fA-F]{3}\-[0-9a-fA-F]{12}$", uuid);
        }
    }
}
