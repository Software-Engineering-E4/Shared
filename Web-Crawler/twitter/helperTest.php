<?php

namespace Tests\Unit;

use Helper;
use Tests\TestCase;

/**
 * Class HelperTest.
 *
 * @covers \Helper
 */
class HelperTest extends TestCase
{
    protected $helper;

    protected function setUp(): void
    {
        parent::setUp();
        $this->helper = new Helper();
    }

    protected function tearDown(): void
    {
        parent::tearDown();

        unset($this->helper);
    }

    /**
     * We need to make sure that there are all parameters that we will set later
     */
    public function testFailure1()
    {
        Assert::assertArrayHasKey('account_id', $this->helper->settings, "Array doesn't contains 'account_id' as key");
    }
    
    public function testFailure2()
    {
        $this->assertArrayHasKey('consumer_key', $this->helper->settings, "Settings doesn't contains 'consumer_key' as key");
    }
    
    public function testFailure3()
    {
        $this->assertArrayHasKey('consumer_secret', $this->helper->settings, "Settings doesn't contains 'consumer_secret' as key");
    }
    
    public function testFailure4()
    {
        $this->assertArrayHasKey('bearer_token', $this->helper->settings, "Settings doesn't contains 'bearer_token' as key");
    }
    
    public function testFailure5()
    {
        $this->assertArrayHasKey('access_token', $this->helper->settings, "Settings doesn't contains 'access_token' as key");
    }
    
    public function testFailure6()
    {
        $this->assertArrayHasKey('access_token_secret', $this->helper->settings, "Settings doesn't contains 'access_token_secret' as key");
    }


    /**
     * We need to make sure that all values in the settings are configured
     */
    public function testFailure7()
    {
        $this->assertNotNull($this->helper->settings['account_id'], "Incomplete settings passed. Expected 'account_id' to have some value");
    }
    
    public function testFailure8()
    {
        $this->assertNotNull($this->helper->settings['consumer_key'], "Incomplete settings passed. Expected 'consumer_key' to have some value");
    }
    
    public function testFailure9()
    {
        $this->assertNotNull($this->helper->settings['consumer_secret'], "Incomplete settings passed. Expected 'consumer_secret' to have some value");
    }
    
    public function testFailure10()
    {
        $this->assertNotNull($this->helper->settings['bearer_token'], "Incomplete settings passed. Expected 'bearer_token' to have some value");
    }
    
    public function testFailure11()
    {
        $this->assertNotNull($this->helper->settings['access_token'], "Incomplete settings passed. Expected 'access_token' to have some value");
    }
    
    public function testFailure12()
    {
        $this->assertNotNull($this->helper->settings['access_token_secret'], "Incomplete settings passed. Expected 'access_token_secret'");
    }

    public function testInsertJsonIntoDB(): void
    {
        /** @todo This test is incomplete. */
        $this->markTestIncomplete();
    }

    public function testGetData(): void
    {
        /** @todo This test is incomplete. */
        $this->markTestIncomplete();
    }
}